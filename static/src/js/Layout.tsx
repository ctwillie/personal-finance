import React from "react";

type LayoutProps = {
  children: React.ReactNode;
};

export default function Layout({ children }: LayoutProps) {
  return (
    <div className="mx-auto max-w-7xl px-4 md:px-6 lg:px-8 py-6 sm:py-8 lg:py-14">
      {children}
    </div>
  );
}
