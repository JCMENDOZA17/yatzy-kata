from Yatzy import Yatzy
import pytest

@pytest.mark.Yatzy
def test_chance_scores_sum_of_all_dice():
        expected = 15
        actual = Yatzy.chance(2,3,4,5,1)
        assert expected == actual
        assert 16 == Yatzy.chance(3,3,4,5,1)
  
@pytest.mark.Yatzy
def test_yatzy_scores_50():
        expected = 50
        actual = Yatzy.yatzy(4,4,4,4,4)
        assert expected == actual
        assert 50 == Yatzy.yatzy(6,6,6,6,6)
        assert 0 == Yatzy.yatzy(6,6,6,6,3)
  
@pytest.mark.Yatzy
def test_1s():
        assert Yatzy.ones(1,2,3,4,5) == 1
        assert 2 == Yatzy.ones(1,2,1,4,5)
        assert 0 == Yatzy.ones(6,2,2,4,5)
        assert 4 == Yatzy.ones(1,2,1,1,1)
  
@pytest.mark.Yatzy
def test_2s():
        assert 4 == Yatzy.twos(1,2,3,2,6)
        assert 10 == Yatzy.twos(2,2,2,2,2)
  
@pytest.mark.Yatzy
def test_threes():
        assert 6 == Yatzy.threes(1,2,3,2,3)
        assert 12 == Yatzy.threes(2,3,3,3,3)
  
@pytest.mark.Yatzy
def test_fours_test():
        assert 12 == Yatzy(4,4,4,5,5).fours()
        assert 8 == Yatzy(4,4,5,5,5).fours()
        assert 4 == Yatzy(4,5,5,5,5).fours()
  
@pytest.mark.Yatzy
def test_fives():
        assert 10 == Yatzy(4,4,4,5,5).fives()
        assert 15 == Yatzy(4,4,5,5,5).fives()
        assert 20 == Yatzy(4,5,5,5,5).fives()
  
@pytest.mark.Yatzy
def test_sixes_test():
        assert 0 == Yatzy(4,4,4,5,5).sixes()
        assert 6 == Yatzy(4,4,6,5,5).sixes()
        assert 18 == Yatzy(6,5,6,6,5).sixes()
  
@pytest.mark.Yatzy
def test_one_pair():
        assert 6 == Yatzy.score_pair(3,4,3,5,6)
        assert 10 == Yatzy.score_pair(5,3,3,3,5)
        assert 12 == Yatzy.score_pair(5,3,6,6,5)
  
@pytest.mark.Yatzy
def test_two_Pair():
        assert 16 == Yatzy.two_pairs(3,3,5,4,5)
        assert 18 == Yatzy.two_pairs(3,3,6,6,6)
        assert 0 == Yatzy.two_pairs(3,3,6,5,4)
  
@pytest.mark.Yatzy
def test_three_of_a_kind():
        assert 9 == Yatzy.three_of_kind(3,3,3,4,5)
        assert 15 == Yatzy.three_of_kind(5,3,5,4,5)
        assert 9 == Yatzy.three_of_kind(3,3,3,3,5)
  
@pytest.mark.Yatzy
def test_four_of_a_knd():
        assert 12 == Yatzy.four_of_kind(3,3,3,3,5)
        assert 20 == Yatzy.four_of_kind(5,5,5,4,5)
        assert 12 == Yatzy.four_of_kind(3,3,3,3,3)
        assert 0  == Yatzy.four_of_kind(3,3,3,2,1)
  
@pytest.mark.Yatzy
def test_smallStraight():
        assert 15 == Yatzy.small_straight(1,2,3,4,5)
        assert 15 == Yatzy.small_straight(2,3,4,5,1)
        assert 0 == Yatzy.small_straight(1,2,2,4,5)
  
@pytest.mark.Yatzy
def test_largeStraight():
        assert 20 == Yatzy.large_straight(6,2,3,4,5)
        assert 20 == Yatzy.large_straight(2,3,4,5,6)
        assert 0 == Yatzy.large_straight(1,2,2,4,5)
  
@pytest.mark.Yatzy
def test_fullHouse():
        assert 18 == Yatzy.full_house(6,2,2,2,6)
        assert 0 == Yatzy.full_house(2,3,4,5,6)