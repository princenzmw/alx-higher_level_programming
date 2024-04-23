# 0x14. JavaScript - Web scraping

for some of the tasks, you will need to install `request` module. You can install it using npm by running `npm install request` in the terminal.

## Resources:books:

Read or watch:

- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)

---

## Learning Objectives:bulb:

What you should learn from this project:

- How to manipulate JSON data
- How to use `request` and fetch API
- How to read and write a file using `fs` module

---

### [0. Readme](./0-readme.js)

Write a script that reads and prints the content of a file.

- The first argument is the file path
- The content of the file must be read in `utf-8`
- If an error occurred during the reading, print the error object
- You must use the `fs` module

Example:

```
$ ./0-readme.js cisfun
C is super fun!
```

---

### [1. Write me](./1-writeme.js)

Write a script that writes a string to a file.

- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in `utf-8`
- If an error occurred during while writing, print the error object
- You must use the `fs` module

Example:

```bash
$ ./1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt ; echo ""
Python is cool

$ ./1-writeme.js my_file.txt "Javascript is amazing"
$ cat my_file.txt ; echo ""
Javascript is amazing
```

---

### [2. Status code](./2-statuscode.js)

Write a script that display the status code of a `GET` request.

- The first argument is the URL to request (`GET`)
- The status code must be printed like this: `code: <status code>`
- You must use the `request` module

Example:

```bash
$ ./2-statuscode.js http://intranet.hbtn.io
code: 200
$ ./2-statuscode.js http://intranet.hbtn.io/doesnt_exist
code: 404
```

---

### [3. Star wars movie title](./3-starwars_title.js)

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- The first argument is the episode number
- You must use the [Star wars API](https://swapi-api.hbtn.io/) with the endpoint https://swapi-api.alx-tools.com/api/films/:id
- You must use the `request` module

Example:

```bash
$ ./3-starwars_title.js 1
A New Hope
$ ./3-starwars_title.js 5
Attack of the Clones
```

---

### [4. Star wars Wedge Antilles](./4-starwars_count.js)

Write a script that prints the number of movies where the character “Wedge Antilles” is present.

- The first argument is the API URL of the [Star wars API](https://swapi-api.alx-tools.com/): https://swapi-api.alx-tools.com/api/films/
- Wedge Antilles is character ID `18` - your script must use this ID for filtering the result of the API
- You must use the `request` module

Example:

```bash
$ ./4-starwars_count.js http://swapi-api.hbtn.io/api/films
3
```

---

### [5. Loripsum](./5-request_store.js)

Write a script that gets the contents of a webpage and stores it in a file.

- The first argument is the URL to request
- The second argument the file path to store the body response
- The file must be UTF-8 encoded
- You must use the `request` module

Example:

```bash
$ ./5-request_store.js http://loripsum.net/api loripsum
$ cat loripsum
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...
```

---

### [6. How many completed?](./6-completed_tasks.js)

Write a script that computes the number of tasks completed by user id.

- The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
- Only print users with completed task
- You must use the `request` module

Example:

```bash
$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{
	"1": 11,
	"2": 8,
	"3": 7,
	"4": 6,
	"5": 12,
	"6": 6,
	"7": 9,
	"8": 11,
	"9": 8,
	"10": 12
}
```

---

### [7. Who was playing in this movie?](./100-starwars_characters.js)

Write a script that prints all characters of a Star Wars movie.

- The first argument is the Movie ID - example: `3` = “Return of the Jedi”
- Display one character name by line
- You must use the [Star wars API](https://swapi-api.hbtn.io/)
- You must use the `request` module

Example:

```bash
$ ./100-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
Admiral Ackbar
```

---

### [8. Right order](./101-starwars_characters.js)

Write a script that prints all characters of a Star Wars movie.

- The first argument is the Movie ID - example: `3` = “Return of the Jedi”
- Display one character name by line **in the same order of the list “characters” in the `/films/` response**
- You must use the [Star wars API](https://swapi-api.hbtn.io/)
- You must use the `request` module

Example:

```bash
$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

---

## Author

- **Prince NZAMUWE** - [princenzmw](https://github.com/princenzmw)
