<p align="center">
<a href="http://dnssijua.com">
<img src="http://dnssijua.com/images/logo-1.png">
</a>
</p>

# De Nobili School, Koradih

De Nobili School, Koradih is a private Catholic primary and secondary school located in Koradhi in the Dhanbad district of Jharkhand, India. Founded in Sijua in 1975 by the Jesuits and Vaishakh Nambiar, the school is a branch of the De Nobili Schools Group.
This python file includes :

- Introduction, origin, and basic infos.


> Note : The teachers list is as of 2018-19.


## Installation

> **Make sure you have python installed.**

```bash
$ git clone https://github.com/advwastaken/DNS

$ cd DNS

$ pip install -r requirements.txt

$ cp src/DNS.py <Your directory path>
```
### Usage

Simply put the `DNS.py` in your project directory and import the `DeNobiliKoradih` class.

```python
from DNS import DeNobiliKoradih
```

### Variables

Example Format :
```python
print(DeNobiliKoradih.intro)
```
Different Variables provided :
| Variable         | Data                                                                                     |
|------------------|------------------------------------------------------------------------------------------|
| intro            | returns some introduction about the school.                                              |
| origin           | returns some information of origin of the school.                                        |
| motto            | returns the motto of the school.                                                         |
| logo             | returns some information about the school's logo.                                        |
| type             | returns the school's types.                                                              |
| website          | returns the school's website.                                                            |
| currentPrincipal | returns the name of the current principal.                                               |
| principals       | returns the names of all the principals since the establishment of the school as a list. |
| board            | returns the school's board (ICSE/CBSE).                                                  |
| schoolSong       | returns the school song.                                                                 |
| teachers         | returns the name of all the teachers as a list.                                          |

### Methods

Example Format :
```python
print(DeNobiliKoradih.getTeachersWith('A'))
```

| Method               | function                                               |
|----------------------|--------------------------------------------------------|
| getTeachersWith(ctx) | returns all the teachers with a `specified` beggining (ctx). |
