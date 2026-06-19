import subprocess

scripts = [
    "clean_competitions",
    "clean_clubs",
    "clean_games",
    "clean_players",
    "clean_appearances",
    "clean_transfers",
    "clean_club_games",
    "clean_game_events",
    "clean_player_valuations"
]

for script in scripts:

    print(f"Running {script}")

    subprocess.run(
        ["python", "-m", f"src.cleaning.{script}"],
        check=True
    )

print("ETL completed")