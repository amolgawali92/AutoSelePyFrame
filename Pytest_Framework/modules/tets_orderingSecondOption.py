import pytest

class TestClass:

    @pytest.mark.run(order=6)
    def test_phase6(self):
        print("Phase 6")

    @pytest.mark.run(order=5)
    def test_phase5(self):
        print("Phase 5")
    @pytest.mark.run(order=4)
    def test_phase4(self):
        print("Phase 4")

    @pytest.mark.run(order=2)
    def test_phase2(self):
        print("Phase 2")

    @pytest.mark.run(order=1)
    def test_phase1(self):
        print("Phase 1")

    @pytest.mark.run(order=3)
    def test_phase3(self):
        print("Phase 3")