import json
import re
import shlex
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

CONTRACT = (
    Path(__file__).resolve().parents[1] / ".agents/contracts/video-to-video-inputs.md"
)


@unittest.skipUnless(
    shutil.which("ffmpeg") and shutil.which("ffprobe"), "requires FFmpeg"
)
class ExactSourceAudioDeliveryTests(unittest.TestCase):
    def test_documented_copy_preserves_independent_stream_spans_and_samples(self):
        with tempfile.TemporaryDirectory() as temporary:

            def ffmpeg(*args):
                return subprocess.check_output(
                    ["ffmpeg", "-v", "error", "-nostdin", *args], cwd=temporary
                )

            def streams(file):
                report = subprocess.check_output(
                    [
                        "ffprobe",
                        "-v",
                        "error",
                        "-show_entries",
                        "stream=codec_type,start_time,duration",
                        "-of",
                        "json",
                        file,
                    ],
                    cwd=temporary,
                )
                return {
                    entry["codec_type"]: (
                        float(entry["start_time"]),
                        float(entry["duration"]),
                    )
                    for entry in json.loads(report)["streams"]
                }

            ffmpeg(
                "-f",
                "lavfi",
                "-i",
                "color=s=32x32:r=10:d=2",
                "-c:v",
                "mpeg4",
                "picture.mov",
            )
            command = re.search(
                r"^```bash\n(ffmpeg [^\n]+)\n```", CONTRACT.read_text(), re.MULTILINE
            )
            if command is None:
                self.fail("expected a runnable compatible MOV delivery example")
            for duration in (1.5, 2.0, 2.5):
                with self.subTest(duration=duration):
                    ffmpeg(
                        "-y",
                        "-f",
                        "lavfi",
                        "-i",
                        f"aevalsrc='if(gt(t,{duration - 0.4}),0.3*sin(2*PI*440*t),0)':s=48000",
                        "-t",
                        str(duration),
                        "-c:a",
                        "pcm_s16le",
                        "recording.wav",
                    )
                    Path(temporary, "delivery.mov").unlink(missing_ok=True)
                    subprocess.run(
                        shlex.split(command[1]),
                        cwd=temporary,
                        check=True,
                        capture_output=True,
                    )
                    self.assertEqual(
                        streams("delivery.mov"),
                        {"video": (0, 2), "audio": (0, duration)},
                    )
                    source = ffmpeg(
                        "-i", "recording.wav", "-map", "0:a:0", "-f", "s16le", "-"
                    )
                    delivered = ffmpeg(
                        "-i", "delivery.mov", "-map", "0:a:0", "-f", "s16le", "-"
                    )
                    self.assertEqual(delivered, source)
                    self.assertNotEqual(set(delivered[-4800:]), {0})
