import { currencyFormatter } from "./value-formatters";

type RecentTransactionsProps = {
  data: Record<string, string | number>[];
};

export default function RecentTransactions({ data }: RecentTransactionsProps) {
  return (
    <div className="relative overflow-x-auto">
      <table className="w-full text-sm text-gray-500">
        <thead className="text-xs text-gray-400">
          <tr>
            <th>Category</th>
            <th>Date</th>
            <th>Amount</th>
          </tr>
        </thead>
        <tbody>
          {data.map((recentTransaction: Record<string, string | number>) => (
            <tr key={recentTransaction.id} className="bg-white">
              <td className="text-gray-800">
                {recentTransaction.category_name}
              </td>
              <td className="py-2">{recentTransaction.date}</td>
              <td className="py-2">
                {currencyFormatter(recentTransaction.amount as number)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
