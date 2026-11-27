import urllib.request
import json

BASE_URL = "http://127.0.0.1:8000"

def test_route(path, expected_status=200):
    url = BASE_URL + path

    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = response.read().decode("utf-8")
            print(f"PASS: {path} | Status: {response.status}")
            print(f"Response: {data}")
            print("-" * 50)

            if response.status != expected_status:
                raise AssertionError(
                    f"Expected status {expected_status}, got {response.status}"
                )

            json.loads(data)

    except Exception as e:
        print(f"FAIL: {path}")
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    test_route("/")
    test_route("/health")
    test_route("/students")

    print("All API tests passed successfully!")