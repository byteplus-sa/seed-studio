import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[1] / ".agents/skills"


class SeedanceFamilyEvidenceTests(unittest.TestCase):
    def text(self, relative):
        return " ".join((SKILLS / relative).read_text().lower().split())

    def test_motion_design_excludes_storyboard_panels_from_conditioning(self):
        text = self.text("seedance-motion-design/SKILL.md")
        self.assertIn("planning-only", text)
        self.assertNotIn("@image 2 defines <approved storyboard", text)
        self.assertNotIn("never stack more than two", text)
        self.assertIn("compatible", text)

    def test_focus_evidence_is_not_a_family_wide_prohibition(self):
        text = self.text("seedance-lens-presets/SKILL.md")
        self.assertNotIn("**post only**", text)
        self.assertNotIn("do not spend more tries", text)
        self.assertIn("model and operation", text)
        self.assertIn("limited evidence", text)
        self.assertNotIn("unverified hypothesis; check a 480p draft", text)

    def test_edit_history_does_not_establish_universal_duration_or_camera_caps(self):
        text = self.text("seedance-vfx-prompt/references/seedance-25-edit.md")
        self.assertNotIn("caps output at ~5s", text)
        self.assertNotIn("keep the camera block to two moves", text)
        self.assertIn("historical", text)
        self.assertIn("model", text)
        self.assertIn("operation", text)

    def test_conform_requires_actual_stream_profile_and_handles_unknown_conflicts(self):
        text = self.text("seedance-vfx-prompt/references/seedance-25-edit.md")
        for concept in ("range", "primaries", "transfer", "matrix",
                        "pixel format", "unknown", "conflicting", "measured"):
            self.assertIn(concept, text)
        self.assertIn("conform", text)
        self.assertIn("not a grade", text)

    def test_slot_mapping_has_no_camera_move_cap(self):
        text = self.text("template-factory/references/slot-mapping.md")
        self.assertNotIn("≤2 moves per shot", text)
        self.assertIn("`seedance-prompt`", text)
        self.assertIn("compatible", text)

    def test_slot_mapping_keeps_all_storyboard_panels_planning_only(self):
        text = self.text("template-factory/references/slot-mapping.md")
        self.assertNotIn("explicitly selected production panel", text)
        self.assertIn("planning-only", text)
        self.assertIn("independently selected", text)

    def test_generic_pacing_does_not_impose_snapshot_duration_or_audio_route(self):
        text = self.text("seedance-pacing-presets/SKILL.md")
        self.assertNotIn("`duration` is within 4-30s", text)
        self.assertNotIn("30s is the ceiling", text)
        self.assertNotIn("lip-sync-critical scenes pair with `seed-audio-prompt`", text)
        self.assertIn("selected model and operation", text)


if __name__ == "__main__":
    unittest.main()
