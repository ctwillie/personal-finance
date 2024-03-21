import { Stat, Transaction } from "@/types";

import { Card, Title } from "@tremor/react";
import SpendByCategoryBarList from "./Charts/SpendByCategoryBarList";
import TransactionsByDay from "./Charts/TransactionsByDay";
import TransactionAmountByDay from "./Charts/TransactionAmountByDay";
import RecentTransactions from "./Charts/RecentTransactions";

type DashboardProps = {
  currentDate: string;
  currentMonth: string;
  overviewStats: Stat[];
  monthlyTransactions: Transaction[];
  monthlySpendByCategory: Record<string, string>[];
  monthlyTransactionsByDay: Record<string, string>[];
  monthlyTransactionAmountByDay: Record<string, string>[];
  monthlyRecentTransactions: Record<string, string>[];
  monthlyTotalTransactions: number;
};

export default function Dashboard(props: DashboardProps) {
  const {
    monthlySpendByCategory,
    monthlyTransactionsByDay,
    monthlyTransactionAmountByDay,
    monthlyTotalTransactions,
    monthlyRecentTransactions,
  } = props;

  return (
    <div className="flex flex-col gap-4 sm:gap-6 lg:gap-y-8">
      {/* Overview Stats */}
      <dl className="grid grid-cols-1 gap-0.5 overflow-hidden rounded-2xl text-center sm:grid-cols-2 lg:grid-cols-4 border bg-white">
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

      <div className="grid lg:grid-cols-2 gap-4 sm:gap-6 lg:gap-8">
        {/* Spend By Category */}
        <Card className="!rounded-2xl">
          <Title className="pb-8">Spend By Category</Title>
          <p className="flex justify-between text-gray-500 mb-3 text-xs">
            <span>Category</span>
            <span>Amount</span>
          </p>
          <SpendByCategoryBarList data={monthlySpendByCategory} />
        </Card>

        {/* Recent Transactions */}
        <Card className="!rounded-2xl">
          <Title className="pb-8">Recent Transactions</Title>
          <RecentTransactions data={monthlyRecentTransactions} />
        </Card>
      </div>

      {/* Transactions By Day */}
      <div className="grid lg:grid-cols-2 gap-4 sm:gap-6 lg:gap-8">
        <Card className="!rounded-2xl">
          <Title className="pb-8">
            Transactions By Day <br />
            <span className="ml-1 text-xs text-gray-500">
              {monthlyTotalTransactions} total transactions
            </span>
          </Title>
          <TransactionsByDay data={monthlyTransactionsByDay} />
        </Card>

        {/* Transactions Amount By Day */}
        <Card className="!rounded-2xl">
          <Title className="pb-8">
            Amount Spent By Day <br />
          </Title>
          <TransactionAmountByDay data={monthlyTransactionAmountByDay} />
        </Card>
      </div>
    </div>
  );
}
