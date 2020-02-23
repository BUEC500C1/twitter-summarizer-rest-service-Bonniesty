import pytest
import getUserTweet2Img as twt_api

def testcase():
    #without twt crudential
    assert twt_api.getUserTwAPI("@AnimalPlanet", "kkk") == "The account or keys is invalid!!"
    assert twt_api.getUserTwAPI("@AnimalPlanet", "123") == "The account or keys is invalid!!"
    assert twt_api.getUserTwAPI("AnimalPlanet", "5567fdgdfgg") == "The account or keys is invalid!!"

    #worng tweeter account name
    assert twt_api.getUserTwAPI("333333", "kkk") == "The account or keys is invalid!!"
    assert twt_api.getUserTwAPI("zcdfgvhv", "kkk") == "The account or keys is invalid!!"
    assert twt_api.getUserTwAPI("886fssfAnimet", "kkk") == "The account or keys is invalid!!"

    #empty crudential
    assert twt_api.getUserTwAPI("@AnimalPlanet", "keys") == ""



if __name__ == '__main__':
    testcase()
