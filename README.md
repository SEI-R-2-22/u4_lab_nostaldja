# Nostaldja Lab

![Nostalgia](https://www.zocalopublicsquare.org/wp-content/uploads/2022/02/nostalgia-L.jpg)

## Overview

In this lab, we'll build an app called Nostaldja, an app for tracking fads across decades.

## Instructions

1. Follow the [installation instructions](https://github.com/SEI-R-11-8/u4_django_install_and_models)
1. Set up your virtual environment and activate it.
1. Install dependencies.
1. Fulfill the listed requirements.



## Setup

Read through the setup instructions from our previous labs

The goal of this app is to have a full-CRUD application with a functioning Admin panel

In your SQL file, create a Database called "Nostaldja", with a user of "NostaldjaUser", and make sure to grant them all permissions

## Requirements

 You'll need to create a new psql database for your app.

### Models

Create two models: `Decade` and `Fad`.

A `Decade` will have `Fad`s, or in other words a fad will have a foreign key for
a decade.

Each Decade should have many Fads (One to Many relationship)

- Decades
  - name ('eighties', 'nineties'...)
  - start_year
  - end_year
- Fads
  - name
  - image_url
  - description
  - decade




## Submission

- Pull request utilizing this template: [PR Guidelines](https://github.com/SEI-R-6-21/template_pull_request)
