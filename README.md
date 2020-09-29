
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Adarshreddyash/ronix-backend">
    <img src="https://raw.githubusercontent.com/Adarshreddyash/background-images-icons/master/play.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">ronix-backend</h3>

  <p align="center">
    BACKEND MUSIC streaming API 
    <br />
    <a href="https://glammingspace.blogspot.com/2020/08/lets-build-music-streaming-app-with.html"><strong>Checkout Step by step tutorial »</strong></a>
    <br />
    <br />
    <a href="https://ronix-backend.herokuapp.com/api/v1/songs">View Demo</a>
    ·
    <a href="https://github.com/Adarshreddyash/ronix-backend/issues">Report Bug</a>
    ·
    <a href="https://github.com/Adarshreddyash/ronix-frontend">Frontend Repo Vuejs</a>
  </p>
</p>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Adarshreddyash/ronix-backend)

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)




<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://raw.githubusercontent.com/Adarshreddyash/ronix-backend/master/media_root/localhost_8080_songs.png)

There arent great tutorials that teaches Django + Vuejs , So, I created this to show the capability of Django and how easy it is to build enterprise level applications with Django and Vuejs.

### Built With
This section lists major frameworks which we used to built this project.
* [Vuejs](https://vuejs.org)
* [Django](https://djangoproject.com)
* [Django REST Framework](https://django-rest-framework.org)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy and running  up  follow these simple steps.

### Prerequisites

We need the following.

* Python3.
* git.

### Installation

1. Clone the repo
```sh
git clone https://github.com/Adarshreddyash/ronix-backend.git
```
2. Install python packages
```sh
pip install -r requirements.txt
```
3. Make migrations
```sh
python manage.py makemigrations
```
4. Run
```sh
python manage.py runserver
```
<!-- USAGE EXAMPLES -->
## Usage {endpoints}

Songs
```sh
127.0.0.1:8000/api/v1/songs
```
Authentication
```sh
127.0.0.1:8000/rest-auth/registration/
127.0.0.1:8000/rest-auth/login/
```
JWT Tokens
```sh
127.0.0.1:8000/api/v1/auth/obtain_token/
127.0.0.1:8000/api/v1/auth/refresh_token/
```
<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Adarshreddyash/ronix-backend/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Twitter - [@adarshreddyash](https://twitter.com/adarshreddyash)

Project Link: [https://github.com/Adarshreddyash/ronix-backend](https://github.com/Adarshreddyash/ronix-backend)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/Adarshreddyash/ronix-backend/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/Adarshreddyash/ronix-backend/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/adarshreddy
[product-screenshot]: images/screenshot.png
