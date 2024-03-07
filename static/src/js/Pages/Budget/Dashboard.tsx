import React from "react";

// TODO: create a prop types
export default function Dashboard(props) {
  return (
    <div className="mx-auto max-w-7xl px-6 lg:px-8">
      <h1 className="text-2xl">Dashboard</h1>
      <br />

      <h5 className="text-lg">
        {props.currentMonth}{" "}
        <span className="text-sm text-gray-500">({props.currentDate})</span>
      </h5>

      {/* Overview Stats */}
      <div className="mx-auto max-w-2xl lg:max-w-none">
        <dl className="mt-16 grid grid-cols-1 gap-0.5 overflow-hidden rounded-2xl text-center sm:grid-cols-2 lg:grid-cols-4">
          {props.overviewStats.map((stat, index) => (
            <div key={index} className="flex flex-col bg-gray-400/5 p-8">
              <dt className="text-sm font-semibold leading-6 text-gray-600">
                {stat.name}
              </dt>
              <dd className="order-first text-3xl font-semibold tracking-tight text-gray-900">
                {stat.value}
              </dd>
            </div>
          ))}
        </dl>
      </div>
    </div>
  );
}
