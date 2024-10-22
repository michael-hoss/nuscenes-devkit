import argparse
from os import path
from typing import Any, Optional
from nuscenes.eval.tracking.tooling.nuscenes_format import TrackingSubmission


class CustomDataEvalConfig:
    def __init__(
        self,
        data_root: str,
        subdir_pattern: Optional[str] = None,
        force_regenerate: bool = False,
        nuscenes_eval_config_path: Optional[str] = None,
    ) -> None:
        """Config for evaluation of nuscenes tracking metrics on own converted data.
        Please read the comments for 
        """

        # Root dir of custom data
        self.data_root: str = data_root

        # Name pattern for nuScenes "version dirs" to evaluate in, as e.g. `v1.0-mini`
        # These subdirs are one level below data_root
        # Wildcards like * and ?? are supported, but not regex.
        self.subdir_pattern: str = subdir_pattern or "*"

        # Force the re-generation of tracking metrics, rather than reading cached metrics from disc.
        self.force_regenerate: bool = force_regenerate

        # Path to JSON config for tracking evaluation, as expected by nuscenes-devkit
        # If None, the default nuscenes config is used
        self.nuscenes_eval_config_path: Optional[str] = nuscenes_eval_config_path

        # Convention for naming of data under test
        self.tracking_results_filename: str = TrackingSubmission.json_filename

        # Store nuScenes data below original data in a subdir
        self.nuscenes_format_root_dir: str = path.join(self.data_root, "nuscenes")

        # Subdir where tracking metrics output files will be saved to
        self.metrics_output_dir: str = "tracking_metrics"

    def get_tracking_result_path(self, subdir_name: str) -> str:
        return path.join(self.nuscenes_format_root_dir, subdir_name, self.tracking_results_filename)

    def get_metrics_output_dir(self, subdir_name: str, eval_split: str) -> str:
        return path.join(self.nuscenes_format_root_dir, subdir_name, self.metrics_output_dir, eval_split)

    def get_splits_filename(self, subdir_name: str) -> str:
        return path.join(self.nuscenes_format_root_dir, subdir_name, "splits.json")

    def get_nuscenes_version_dir(self, subdir_name: str) -> str:
        return path.join(self.nuscenes_format_root_dir, subdir_name)

    @staticmethod
    def read_cli() -> Any:
        parser = argparse.ArgumentParser(
            description="Arguments to specify the evaluation of 3D MOT metrics on custom data using the nuscenes-devkit fork."
        )

        parser.add_argument(
            "--data-root",
            type=str,
            help="Root directory to the custom data",
        )
        parser.add_argument(
            "--force-regenerate",
            action="store_true",
            help="If flag is set, regenerates all metrics from scratch",
        )

        parser.add_argument(
            "--subdir-pattern",
            type=str,
            help="Name pattern for individual subdirectories of data-root to be evaluated.",
        )

        parser.add_argument(
            "--nuscenes-eval-config-path",
            type=str,
            help="Path to the config file for the nuscenes tracking evaluation",
        )

        args = parser.parse_args()
        return args

    @staticmethod
    def from_cli() -> "CustomDataEvalConfig":
        args = CustomDataEvalConfig.read_cli()
        conversion_config = CustomDataEvalConfig(
            data_root=args.data_root,
            subdir_pattern=args.subdir_pattern,
            force_regenerate=args.force_regenerate,
            nuscenes_eval_config_path=args.nuscenes_eval_config_path,
        )
        return conversion_config
