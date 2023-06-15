# Workout App
#### Comp 437 term project by Özlem Şerifoğulları
## Project Description
The aim of this project is to provide an app for people who wants to follow a training process on their own at home. The app will provide training videos, and real-time feedback for the movements with pose estimation. The app, also will provide profile page for user to share their interests, agenda for user to schedule and follow their training, and background changing for user to feel like in a different envrionment from home.
## Challenges
### Swift MacOS App
I didn't know swift language before I started to this project, that's why learning and completing complex tasks became hard for me. I sometimes got some errors that is not handled or mentioned the tutorial I followed. The community of swift is not so big; therefore, I couldn't take help for the errors I got. I also have hard time using navigation views and navigating between different views. I couldn't totally understand the logic, and I couldn't make it work as I wanted.
### Embed Python Code in SwiftUI
After I tried and fail to start camera in swift, I decided to use python script and embed it into swift app because there was much more source in python not just for starting camera but also for background changing, and  pose estimation. However, embedding python code in a swift app was not easy and as new learner for swift I couldn't achieved. Hence, I had seperate applications for the app and the python script that makes background chagning and pose estimation.
### Using pose estimation and changing background together
To see clearly I implemented a code that shows the camera view both with and without changed background. We can clearly see that the pose estimation is not working properly while the background change is on. However, this problem may be handled with using the pose estimation information from the screen without background changing.
## What have I learned?
### Swift and SwiftUI
I learned how to make a simple macOS app using Swift and SwiftUI. I learned the language basics and some logic.
### opencv and cvzone
I learned starting camera, capturing and showing real-time video from camera with using opencv. I learned how to change background and use pose estimation with cvzone.
### PythonKit
Even if I couldn't achieve to embed python code in a swift app I read lots of tutorials and documentation about PythonKit and embedding python in swift. I understand and learned the some basics but not all.
## Suggestions
For the future contributers, embedding python script to workout app would be a good start. After this the real-time feedback should be added to the properties. Finally, working on the details of the app, adding new backgrounds, and training videos can be helpful.
