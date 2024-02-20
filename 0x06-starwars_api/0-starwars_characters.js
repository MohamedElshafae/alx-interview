#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;
    for (const characterUrl of characters) {
      const name = await fetchName(characterUrl);
      console.log(name);
    }
  } else {
    console.error(res.statusCode);
  }
});

async function fetchName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      if (response.statusCode !== 200) {
        reject(response.statusCode);
        return;
      }
      const characterData = JSON.parse(body);
      resolve(characterData.name);
    });
  });
}
