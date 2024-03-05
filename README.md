## Todo

- [ ] Persist the access token on the item record
  - [ ] Use the access token to make api requests

## Budget Questions

- What was the total amount spent during a specific time period?
- What is the average amount spent per transaction?
- Which category/subcategory has the highest total spending?
- How much was spent on groceries in a particular month?
- What was the average spending on entertainment per month?
- How much money was spent on utilities over the past year?
- What percentage of total expenses does each category/subcategory represent?
- How many transactions were made in a certain category/subcategory?
- What was the largest single transaction amount?
- What is the trend in spending over the past few months?
- How much was spent on transportation in a specific quarter?
- What percentage of income was spent on rent/mortgage?
- How many transactions were made in cash versus card payments?
- What was the total amount of income received in a given period?
- How much was spent on dining out versus cooking at home?
- What was the average spending per day of the week?
- How much money was saved in a particular savings account over time?
- What were the top three expense categories for the year?
- How much was spent on non-essential items versus essentials?
- What is the ratio of fixed expenses to variable expenses?

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
