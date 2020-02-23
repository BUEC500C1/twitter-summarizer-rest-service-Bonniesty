import pytest
import getUserTweet2Img as twt_api

def testcase_twt():
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
    assert twt_api.getUserTwAPI("@cnnbrk", "keys") == ""

def testcase_creat_image():
    #test convert text to image
    assert twt_api.text2img("Hello This is test case no.1 text!!!", "test", 11) == "Image Generated!!"
    assert twt_api.text2img("qweeffvcvd!!!", "12313", 2) == "Image Generated!!"
    assert twt_api.text2img("dfgfhhjskkdkslsksj36738222k!!!", "tefd2e43st", 7) == "Image Generated!!"
    assert twt_api.text2img("ghjkljhgjkhnsnahsskas", "t6%4251st", 19) == "Image Generated!!"
    assert twt_api.text2img("Helllo This is test case no.4 text!!!", "666612ddd", 2) == "Image Generated!!"



if __name__ == '__main__':
    testcase_twt()
    testcase_creat_image()
