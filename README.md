# HW4 FFmpeg


## Task:
1. Step 1: Develop a queue system that can exercise your requirements with stub functions.
2. Step 2: Develop the twitter functionality with an API
3. Step 3: Integrate them


Main Exercise:
Using the twitter feed, construct a daily video summarizing a twitter handle day


1. Convert text into an image in a frame
2. Do a sequence of all texts and images in chronological order.
3. Display each video frame for 3 seconds

## Computional question
How many API calls you can handle simultaneously and why? For example, run different API calls at the same time? Split the processing of an API into multiple threads?


My computer has 4-core cpu and each core has two threads and it has hyper-threading. So it can handle 8 threads simultaneously. If one thread run one API, then it can handle 8 APIs at the same time. If split an API to 2 threads, it can run 4 APIs at the same time.

## How to run
This is a queue system that can fetch twitter feed text of one account, convert top 20 twitter feed text as well as pictures to image and generated image to a video. This video display each frame for 3 seconds.

### Structure:
There are three python files

```tweetImg2Video.py```: fetch twitter feed, convet feed text to image frame, downloaded image (including pictures inside twitter feed) to ```textImage``` folder.

```getUserTweet2Img.py```: read images of previous step, resize them and use FFmpeg to convert them to video. This video display each image for three seconds.

```main.py```: a queue system which allowed multithreading to call the two APIs.

### Install:
1. Enter your twitter credential in ```keys```.
2. Install packages in keys
3. Replace font path in ```getUserTweet2Img.py``` line 25. Or if you are using Mac PC, you don't need to do this.
4. You can modify ```nameList``` and entering valid twitter account name. And run:
  ```python
  python main.py
  ```
Also, you can modify account name in ```getUserTweet2Img.py``` and ```tweetImg2Video.py```. And run seperately.

5. Then, text converted to image frame will stored in ```textImage``` folder. Images prepared to generate video will stored in ```ToVideoTweet``` folder. And video will be downloaded as ```tweetVideo@AccountName.mp4```

## Example

Image of twitter account(In ```textImage``` folder):
@AnimalPlanet

![image](https://github.com/BUEC500C1/video-Bonniesty/blob/master/textImage/%40AnimalPlanetpic000.png)
![image](https://github.com/BUEC500C1/video-Bonniesty/blob/master/textImage/%40AnimalPlanetpic001.png)

@cnnbrk

![image](https://github.com/BUEC500C1/video-Bonniesty/blob/master/textImage/%40cnnbrkpic000.png)
![image](https://github.com/BUEC500C1/video-Bonniesty/blob/master/textImage/%40cnnbrkpic001.png)
