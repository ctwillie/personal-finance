import { Link } from "@inertiajs/react";
import React from "react";

export default function Index() {
  return (
    <div className="divide-y divide-gray-200 overflow-hidden rounded-lg bg-gray-200 shadow sm:grid sm:grid-cols-2 sm:gap-px sm:divide-y-0">
      <div className="group relative bg-white p-6">
        <div>
          <span className="inline-flex rounded-lg bg-yellow-50 p-3 text-yellow-700 ring-4 ring-white">
            <svg
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              strokeWidth="1.5"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M2.25 18.75a60.07 60.07 0 0115.797 2.101c.727.198 1.453-.342 1.453-1.096V18.75M3.75 4.5v.75A.75.75 0 013 6h-.75m0 0v-.375c0-.621.504-1.125 1.125-1.125H20.25M2.25 6v9m18-10.5v.75c0 .414.336.75.75.75h.75m-1.5-1.5h.375c.621 0 1.125.504 1.125 1.125v9.75c0 .621-.504 1.125-1.125 1.125h-.375m1.5-1.5H21a.75.75 0 00-.75.75v.75m0 0H3.75m0 0h-.375a1.125 1.125 0 01-1.125-1.125V15m1.5 1.5v-.75A.75.75 0 003 15h-.75M15 10.5a3 3 0 11-6 0 3 3 0 016 0zm3 0h.008v.008H18V10.5zm-12 0h.008v.008H6V10.5z"
              />
            </svg>
          </span>
        </div>
        <div className="mt-8">
          <h3 className="text-base font-semibold leading-6 text-gray-900">
            <Link href="/budget/transactions" className="focus:outline-none">
              <span className="absolute inset-0" aria-hidden="true"></span>
              Transactions
            </Link>
          </h3>
          <p className="mt-2 text-sm text-gray-500">
            View all your transactions in one place. See where your money is
            going.
          </p>
        </div>
        <span
          className="pointer-events-none absolute right-6 top-6 text-gray-300 group-hover:text-gray-400"
          aria-hidden="true"
        >
          <svg className="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M20 4h1a1 1 0 00-1-1v1zm-1 12a1 1 0 102 0h-2zM8 3a1 1 0 000 2V3zM3.293 19.293a1 1 0 101.414 1.414l-1.414-1.414zM19 4v12h2V4h-2zm1-1H8v2h12V3zm-.707.293l-16 16 1.414 1.414 16-16-1.414-1.414z" />
          </svg>
        </span>
      </div>

      <div className="group relative rounded-tl-lg rounded-tr-lg bg-white p-6 sm:rounded-tr-none">
        <div>
          <span className="inline-flex rounded-lg bg-teal-50 p-3 text-teal-700 ring-4 ring-white">
            <svg
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              strokeWidth="1.5"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </span>
        </div>
        <div className="mt-8">
          <h3 className="text-base font-semibold leading-6 text-gray-900">
            <a href="/budget" className="focus:outline-none">
              <span className="absolute inset-0" aria-hidden="true"></span>
              Dashboard
            </a>
          </h3>
          <p className="mt-2 text-sm text-gray-500">
            Get in control of your finances! Start by knowing where your money
            goes and how much you have left to spend.
          </p>
        </div>
        <span
          className="pointer-events-none absolute right-6 top-6 text-gray-300 group-hover:text-gray-400"
          aria-hidden="true"
        >
          <svg className="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
            <path d="M20 4h1a1 1 0 00-1-1v1zm-1 12a1 1 0 102 0h-2zM8 3a1 1 0 000 2V3zM3.293 19.293a1 1 0 101.414 1.414l-1.414-1.414zM19 4v12h2V4h-2zm1-1H8v2h12V3zm-.707.293l-16 16 1.414 1.414 16-16-1.414-1.414z" />
          </svg>
        </span>
      </div>
    </div>
  );
}
