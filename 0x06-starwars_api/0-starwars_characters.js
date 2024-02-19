#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;
    characters.forEach((characterUrl) => {
      request(characterUrl, (err, res, body) => {
        if (err) {
          console.error(err);
          return;
        }

        if (res.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.error(res.statusCode);
  }
});
