import { Stat, Transaction } from "@/types";

import { Card, Title } from "@tremor/react";
import SpendByCategoryBarList from "./Charts/SpendByCategoryBarList";
import TransactionsByDay from "./Charts/TransactionsByDay";

type DashboardProps = {
  currentDate: string;
  currentMonth: string;
  overviewStats: Stat[];
  monthlyTransactions: Transaction[];
  monthlySpendByCategory: Record<string, string>[];
  monthlyTransactionsByDay: Record<string, string>[];
};

export default function Dashboard(props: DashboardProps) {
  const { monthlySpendByCategory, monthlyTransactionsByDay } = props;

  return (
    <div>
      <h1 className="text-2xl">Dashboard</h1>
      <br />

      <h5 className="text-lg">
        {props.currentMonth}{" "}
        <span className="text-sm text-gray-500">({props.currentDate})</span>
      </h5>

      {/* Overview Stats */}
      <dl className="mt-16 grid grid-cols-1 gap-0.5 overflow-hidden rounded-2xl text-center sm:grid-cols-2 lg:grid-cols-4 border">
        {props.overviewStats.map((stat, index) => (
          <div key={index} className="flex flex-col p-8">
            <dt className="text-sm font-semibold leading-6 text-gray-600">
              {stat.name}
            </dt>
            <dd className="order-first text-3xl font-semibold tracking-tight text-gray-900">
              {stat.value}
            </dd>
          </div>
        ))}
      </dl>

      {/* Spend By Category */}
      <Card className="my-8 lg:w-1/2 !rounded-2xl">
        <Title className="pb-8">Spend By Category</Title>
        <p className="flex justify-between text-gray-500 mb-3 text-sm">
          <span>Category</span>
          <span>Amount</span>
        </p>
        <SpendByCategoryBarList data={monthlySpendByCategory} />
      </Card>

      {/* Transactions By Day */}
      <Card className="my-8 !rounded-2xl">
        <Title className="pb-8">Transactions By Day</Title>
        <TransactionsByDay data={monthlyTransactionsByDay} />
      </Card>
    </div>
  );
}
