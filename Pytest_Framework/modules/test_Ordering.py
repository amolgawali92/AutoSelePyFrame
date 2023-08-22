import py_compile

import pytest

class TestClass:

    @pytest.mark.sixth
    def test_phase6(self):
        print("Phase 6")

    @pytest.mark.fifth
    def test_phase5(self):
        print("Phase 5")
    @pytest.mark.fourth
    def test_phase4(self):
        print("Phase 4")

    @pytest.mark.second
    def test_phase2(self):
        print("Phase 2")

    @pytest.mark.first
    def test_phase1(self):
        print("Phase 1")

    @pytest.mark.third
    def test_phase3(self):
        print("Phase 3")