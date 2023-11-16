## 1

Для запуска тестирования doctest используется данная команда:

```commandline
python -m doctest -o IGNORE_EXCEPTION_DETAIL -v morse.py
```

## 2

Для запуска тестирования pytest.mark.reparametrized используется данная команда:

```commandline
python -m pytest -v tests/test_decode.py
```

## 3

Unittest тестирование запускается при помощи такой команды:

```commandline
python -m unittest -v tests/test_ohe_unittest.py
```


