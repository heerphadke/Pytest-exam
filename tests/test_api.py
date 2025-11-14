import subprocess, time, requests, sys, pytest

BASE = "http://127.0.0.1:5000"

@pytest.fixture(scope="session", autouse=True)
def server(): 
    p = subprocess.Popen([sys.executable, "app.py"])
    time.sleep(1)
    yield
    p.terminate()

def test_status():
    r = requests.get(f"{BASE}/status")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_sum():
    r = requests.get(f"{BASE}/sum?a=2&b=3")
    assert r.status_code == 200
    assert r.json() == {"result": 5}
