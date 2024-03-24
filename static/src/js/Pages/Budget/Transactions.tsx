import * as React from "react";

import {
  PaginationState,
  createColumnHelper,
  flexRender,
  getCoreRowModel,
  useReactTable,
} from "@tanstack/react-table";
import { Card, Title } from "@tremor/react";
import { currencyFormatter } from "./Charts/value-formatters";
import { keepPreviousData, useQuery } from "@tanstack/react-query";

type Transaction = {
  id: number;
  categoryName: string;
  amount: number;
  description: string;
  date: string;
};

type TransactionQueryData = {
  transactions: Transaction[];
  pageCount: number;
};

const columnHelper = createColumnHelper<Transaction>();

const columns = [
  columnHelper.accessor("categoryName", {
    cell: (info) => info.getValue(),
    header: () => <span>Category</span>,
    footer: (info) => info.column.id,
  }),
  columnHelper.accessor("amount", {
    cell: (info) => <span>{currencyFormatter(info.getValue())}</span>,
    header: () => <span>Amount</span>,
    footer: (info) => info.column.id,
  }),
  columnHelper.accessor("description", {
    cell: (info) => info.getValue(),
    header: () => <span>Description</span>,
    footer: (info) => info.column.id,
  }),
  columnHelper.accessor("date", {
    cell: (info) => info.getValue(),
    header: () => <span>Date</span>,
    footer: (info) => info.column.id,
  }),
];

export default function Transactions() {
  const defaultData = React.useMemo(() => [], []);
  const [pagination, setPagination] = React.useState<PaginationState>({
    pageIndex: 0,
    pageSize: 10,
  });

  const getTransactions = async () => {
    const { pageIndex, pageSize } = pagination;
    const response = await fetch(
      `http://localhost:8000/budget/transactions/list?pageIndex=${pageIndex}&pageSize=${pageSize}`
    );

    return response.json();
  };

  const query = useQuery<TransactionQueryData>({
    queryKey: ["transactions", pagination],
    queryFn: getTransactions,
    placeholderData: keepPreviousData,
  });

  const table = useReactTable<Transaction>({
    data: query.data?.transactions ?? defaultData,
    columns,
    pageCount: query.data?.pageCount ?? -1,
    state: { pagination },
    onPaginationChange: setPagination,
    getCoreRowModel: getCoreRowModel(),
    manualPagination: true,
  });

  if (query.isLoading) {
    return null;
  }

  return (
    <Card className="!rounded-2xl">
      <Title className="pb-8">Transactions</Title>
      <div className="px-4 sm:px-6 lg:px-8">
        <div className="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div className="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
            <table className="min-w-full divide-y divide-gray-300">
              <thead>
                {table.getHeaderGroups().map((headerGroup) => (
                  <tr key={headerGroup.id}>
                    {headerGroup.headers.map((header) => (
                      <th
                        scope="col"
                        className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                        key={header.id}
                      >
                        {header.isPlaceholder
                          ? null
                          : flexRender(
                              header.column.columnDef.header,
                              header.getContext()
                            )}
                      </th>
                    ))}
                  </tr>
                ))}
              </thead>
              <tbody>
                {table.getRowModel().rows.length > 0 ? (
                  table.getRowModel().rows.map((row) => (
                    <tr key={row.id}>
                      {row.getVisibleCells().map((cell) => (
                        <td
                          key={cell.id}
                          className="whitespace-nowrap px-3 py-4 text-sm text-gray-500"
                        >
                          {flexRender(
                            cell.column.columnDef.cell,
                            cell.getContext()
                          )}
                        </td>
                      ))}
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td>No results to show</td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <nav className="flex items-center justify-between border-t border-gray-200 bg-white px-4 pt-4 sm:px-6">
        <div className="hidden sm:block">
          <p className="text-sm text-gray-700">
            Page{" "}
            <span className="font-medium">
              {table.getState().pagination.pageIndex + 1}
            </span>{" "}
            of <span className="font-medium">{table.getPageCount()}</span>
          </p>
        </div>
        <div className="flex flex-1 justify-between sm:justify-end">
          <button
            className="relative inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus-visible:outline-offset-0"
            onClick={() => table.previousPage()}
            disabled={!table.getCanPreviousPage()}
          >
            Previous
          </button>
          <button
            className="relative ml-3 inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus-visible:outline-offset-0"
            onClick={() => table.nextPage()}
            disabled={!table.getCanNextPage()}
          >
            Next
          </button>
        </div>
      </nav>
    </Card>
  );
}
