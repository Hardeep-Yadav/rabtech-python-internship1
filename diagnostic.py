import json
import os

filename = "diagnostic-events .json"

print("=== Diagnostic Tool ===")

if os.path.exists(filename):
    print("JSON file found!")

    with open(filename, "r") as file:
        data = json.load(file)

    print("Total events:", len(data["events"]))

    print("\n=== Event Details ===")

    for event in data["events"]:
        print(
            event.get("timestamp"),
            "|",
            event.get("service"),
            "|",
            event.get("level"),
            "|",
            event.get("latency_ms"),
            "|",
            event.get("status_code")
        )

    print("\n=== Analysis ===")

    errors = 0
    warnings = 0
    successful = 0
    failed = 0

    for event in data["events"]:
        if event.get("level") == "ERROR":
            errors += 1

        if event.get("level") == "WARN":
            warnings += 1

        status = event.get("status_code")

        if status >= 200 and status < 300:
            successful += 1
        else:
            failed += 1

    print("Errors:", errors)
    print("Warnings:", warnings)
    print("Successful:", successful)
    print("Failed:", failed)

    print("\n=== Test Completed ===")
    print("Diagnostic tool executed successfully.")

else:
    print("JSON file not found!")
