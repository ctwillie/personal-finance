## Todo

- [ ] Persist the access token on the item record
  - [ ] Use the access token to make api requests

## References

- [Plaid API](https://plaid.com/docs/api/)
- [Pattern - example project](https://github.com/plaid/pattern)
- Inertia Setup
  - [Youtube Guide](https://www.youtube.com/watch?app=desktop&v=7LOwMd662Hw)
  - [Github django-vite](https://github.com/MrBin99/django-vite?tab=readme-ov-file#examples)
  - [Github inertia-django](https://github.com/inertiajs/inertia-django?tab=readme-ov-file)

# Vite/React

- https://gist.github.com/lucianoratamero/7fc9737d24229ea9219f0987272896a2

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
