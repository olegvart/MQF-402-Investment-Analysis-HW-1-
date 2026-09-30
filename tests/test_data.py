from mqf_hw1.data import load_data

def test_data_loads():
    df = load_data()
    assert not df.empty