import { createInertiaApp } from "@inertiajs/react";
import { createRoot } from "react-dom/client";

import "../css/style.css";
import Layout from "./Layout";

createInertiaApp({
  resolve: (name) => {
    const pages = import.meta.glob("./Pages/**/*.tsx", { eager: true });
    const page = pages[`./Pages/${name}.tsx`];

    // Apply a default layout if not specified
    page.default.layout =
      page.default.layout || ((page) => <Layout children={page} />);

    return page;
  },
  setup({ el, App, props }) {
    createRoot(el).render(<App {...props} />);
  },
});
