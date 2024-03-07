# Look Inside View

![look-inside-view-logo](https://user-images.githubusercontent.com/51036153/131473260-eaa32f95-1328-4115-9f0e-73c5ef4ccb3f.png)

## introduction

This website is showing inside of Sakaehigashi high & junior high school by using 360° image.

Please set the root directory `public`.

## features

### about gyro sensor

If your device has gyro sensor, tap the most right icon and tilt your device, then you can see around.

### full screen mode

tap second from the right icon, the image area will be wider.

caution: this function can't use on iPhone. You can check [here](https://caniuse.com/fullscreen) which environment support full screen mode.

## maintenance

### generate secret key for running Python

1. Open https://console.firebase.google.com/u/0/project/look-inside-view/settings/serviceaccounts/adminsdk?hl=ja
1. Click "Generate new private key" button
1. Set credential file to root directory and rename it to `look-inside-view-firebase-adminsdk.json`
