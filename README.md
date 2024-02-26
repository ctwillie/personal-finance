## Todo

- [ ] Persist the access token on the item record
    - [ ] Use the access token to make api requests


## References

- [Plaid API](https://plaid.com/docs/api/)
- [Pattern - example project](https://github.com/plaid/pattern)


## Database Seeding

- To seed budget items and accounts:
```bash
python manage.py seeditemsandaccounts
```

- To seed budget categories:
```bash
python manage.py seedcategories
```

- To seed budget transactions:
```bash
python manage.py seedtransactions
```

- To update budget transactions:
```bash
python manage.py updatetransactions
```
