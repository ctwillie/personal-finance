import { Link } from "@inertiajs/react";
import React from "react";

export default function Home() {
  return (
    <>
      <div className="flex flex-col items-center">
        <h1 className="text-4xl font-bold">Personal Finance</h1>
        <p className="mt-4 text-lg">A simple budgeting app</p>
      </div>

      <footer className="absolute bottom-0 left-40 bg-white">
        <div className="mx-auto max-w-7xl overflow-hidden px-6 py-20 sm:py-24 lg:px-8">
          <nav
            className="-mb-6 columns-2 sm:flex sm:justify-center sm:space-x-12"
            aria-label="Footer"
          >
            <div className="pb-6">
              <Link
                href="/"
                className="text-sm leading-6 text-gray-600 hover:text-gray-900"
              >
                Home
              </Link>
            </div>
            <div className="pb-6">
              <Link
                href="/budget"
                className="text-sm leading-6 text-gray-600 hover:text-gray-900"
              >
                Budget
              </Link>
            </div>
          </nav>
        </div>
      </footer>
    </>
  );
}
