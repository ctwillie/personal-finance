export type Stat = {
  name: string;
  value: string | number;
};

export type Transaction = {
  id: number;
  date: string;
  description: string;
  category: string;
  amount: number;
};
