"""Enveloppe de sim_full_system.launch.py pour le débogage VS Code (simulation, sans LiDAR ni GPS).

À placer dans ~/mowglinext/.vscode/sim_debug.launch.py
Cible de la configuration launch.json "ROS2: Simulation complète (tous les noeuds)".
"""
import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

# .vscode/ -> racine du dépôt -> ros2/install/...
_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_SIM_LAUNCH = os.path.join(
    _REPO, "ros2", "install", "mowgli_bringup", "share", "mowgli_bringup",
    "launch", "sim_full_system.launch.py",
)


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(_SIM_LAUNCH),
            launch_arguments={
                # Pas de LiDAR ni de GPS en simulation
                "use_lidar": "false",
                "use_gps_dock_detection": "false",
                # Valeurs recommandées en simulation par les descriptions du launch
                "use_sim_time": "true",
                "cog_stationary_seed_rate_hz": "0.0",
                "fusion_graph_tf_lead_s": "0.1",
                "tf_publish_lead_s": "0.1",
                "node_period_s": "0.02",
            }.items(),
        ),
    ])
