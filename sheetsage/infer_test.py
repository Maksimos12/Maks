import ast
import unittest

from .assets import retrieve_asset
from .infer import InputFeats, OutputModality, sheetsage

_FISHIN_VERIFIED = """
(((0, (4, 2, 2)),), ((0, (120,)),), ((0, (10, (2, 2, 1, 2, 2, 2))),), ((0, (10, (4, 3))), (96, (3, (4, 3))), (128, (10, (4, 3))), (224, (3, (4, 3)))), ((0, 4, (0, 5)), (4, 4, (5, 5)), (8, 4, (5, 5)), (12, 2, (5, 5)), (14, 2, (0, 5)), (16, 2, (7, 5)), (18, 4, (5, 5)), (22, 4, (5, 5)), (26, 2, (2, 5)), (28, 4, (2, 5)), (32, 12, (0, 5)), (44, 12, (10, 4)), (56, 4, (5, 5)), (60, 14, (2, 5)), (74, 6, (2, 5)), (80, 10, (5, 5)), (90, 38, (2, 5)), (128, 4, (2, 5)), (132, 4, (5, 5)), (136, 2, (5, 5)), (138, 2, (5, 5)), (140, 8, (5, 5)), (148, 4, (5, 5)), (152, 2, (5, 5)), (154, 2, (2, 5)), (156, 4, (2, 5)), (160, 4, (0, 5)), (164, 4, (0, 5)), (168, 2, (0, 5)), (170, 2, (10, 4)), (172, 4, (10, 4)), (176, 4, (2, 5)), (180, 1, (5, 5)), (181, 3, (5, 5)), (184, 4, (5, 5)), (188, 4, (2, 5)), (192, 10, (10, 4)), (202, 54, (2, 5)), (256, 16, (7, 5))), 272)
""".strip()


class TestSheetSage(unittest.TestCase):
    def test_sheetsage(self):
        lead_sheet = sheetsage(
            retrieve_asset("TEST_FISHIN"),
            input_feats=InputFeats.HANDCRAFTED,
            output_modality=OutputModality.LEAD_SHEET,
            segment_start_hint=11,
            segment_end_hint=11 + 23.75,
            measures_per_segment=17,
        )
        self.assertEqual(lead_sheet, ast.literal_eval(_FISHIN_VERIFIED))