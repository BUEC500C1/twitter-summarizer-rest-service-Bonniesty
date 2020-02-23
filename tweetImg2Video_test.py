import pytest
import tweetImg2Video as video_api

def testcase():
    #test resize image
    assert video_api.process_img("@AnimalPlanet") == "Image Resized!!"
    assert video_api.process_img("@cnnbrk") == "Image Resized!!"

    #test create video
    assert video_api.toVideo("@cnnbrk") == "Video Created!!"
    assert video_api.toVideo("@AnimalPlanet") == "Video Created!!"

    #test wrong cases
    assert video_api.toVideo("@qqqq") == "Fail!!!"
    assert video_api.toVideo("@qqwedw") == "Fail!!!"
    assert video_api.toVideo("@!!24rfs") == "Fail!!!"


if __name__ == '__main__':
    testcase()
