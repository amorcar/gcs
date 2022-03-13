# GCS
A ground control station for configuring and monitorizing drone flights


- [ ] ~~Vue frontend feeded by a python application communcated via zerorpc, as common http api calls are unefficient for inter-process communication.~~
- [x] Vue frontend feeded by a python application communcated via http api calls.

#### Installation of Vue + Electron
This is a template to create a **NEW** vue + electron apps. Not the steps to install this project.
To initialize this project refer to the gcs/README.md instructions.

> Ensure nodejs and vue/cli are already installed

Initialize vue app and install electron as a project dependency:
```
$ vue create gcs
$ cd gcs
$ npm run serve # check everything is working
$ vue add vuetify
$ npm install --save-dev electron@latest
$ vue add electron-builder
```

If using multiple pages (views, navigation)
```
$ npm install axios
```

Create a `main.js` file in the vue app (gcs) with this content:
```
const { app, BrowserWindow } = require('electron');

const url = require("url");
const path = require("path");

let mainWindow

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  })

  mainWindow.loadURL(
    url.format({
      pathname: path.join(__dirname, `./dist/index.html`),
      protocol: "file:",
      slashes: true
    })
  );
  mainWindow.on('closed', function () {
    mainWindow = null
  })
}
console.log(app);
app.on('ready', createWindow)

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', function () {
  if (mainWindow === null) createWindow()
})
```

Add `main.js` as entrypoin by adding `"main": "main.js"` to `packacge.json` file.

Edit `vue.config.js` and add this:

```
module.exports  = {
    publicPath: process.env.NODE_ENV  ===  'production'  ?  './'  :  '/'
}
```

Run and check everything is working:

```
$ npm start
```

#### Useful links

- [Building a Desktop App with Electron and Vue.js](https://buddy.works/tutorials/building-a-desktop-app-with-electron-and-vue-js)
- [Vuetify](https://vuetifyjs.com/en/getting-started/installation/)
- [Getting started with Vuex: A beginners guide](https://codesource.io/getting-started-with-vuex-a-beginners-guide/)
- [Electron as GUI of Python Applications](https://github.com/fyears/electron-python-example)
- [Geoman-io leaflet plugin](https://github.com/geoman-io/leaflet-geoman#installation)



