# *Application Name*
## Agrithon 2020

### About
A mobile application that provides farmers with the following facilities.

- Disease Recognition through image search.
- Provides remedies, giving preference to locally available methods.
- A dedicated compendium of diseases and pests and ways to counteract them.
- Shows weather reports, alerting of severe conditions.
- Local news section, which reports on agricultural policies, signs of pests / disease, insights into price of various crops.

## Implementation
The smart phone application will be built on flutter, a cross platform UI. It will be written in dart.
It will connect to a flask server, where the main application resides. 

The user will take a photo of the afflicted crop using their phone and it will be sent to a flask server through a flutter API 
and an image search will be done by a python based Content Based Image Retrieval (CBIR). After finding the best match, it will 
send the information back to mobile application along with suggested remedies, pesticides or other steps.

## Advantages
- The app will have an intuitive UI as well as regional language support.
- It will provide farmers with a whole suite of information, all in one place.
- Since it's built in flutter, it will be cross platform and can be extended to many devices.

## Disadvantages
- The user needs to have a smart phone and a bare minimum knowledge of how to use it.
- Image recognition might not always be 100% accurate.
- The application needs to be constantly updated with the relevant details.
