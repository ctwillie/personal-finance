import { resolve } from "path";
import { defineConfig } from "vite";

import react from "@vitejs/plugin-react";

// export default defineConfig({
//   resolve: {
//     alias: {
//       src: resolve(__dirname, "src"),
//     },
//   },
//   esbuild: {
//     loader: "jsx",
//     include: /src\/.*\.jsx?$/,
//     exclude: [],
//   },
//   optimizeDeps: {
//     esbuildOptions: {
//       plugins: [
//         {
//           name: "load-js-files-as-jsx",
//           setup(build) {
//             build.onLoad({ filter: /src\\.*\.js$/ }, async (args) => ({
//               loader: "jsx",
//               contents: await fs.readFile(args.path, "utf8"),
//             }));
//           },
//         },
//       ],
//     },
//   },
//   plugins: [react()],
// });

export default defineConfig({
  plugins: [
    react({
      // jsxRuntime: "classic",
      // babel: {
      //   plugins: ["styled-jsx/babel"],
      // },
    }),
  ],
  root: resolve("./static/src"),
  base: "/static/",
  server: {
    host: "localhost",
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  resolve: {
    extensions: [".js", ".json"],
  },
  esbuild: {
    loader: "jsx",
    include: /src\/.*\.jsx?$/,
    exclude: [],
  },
  build: {
    outDir: resolve("./static/build"),
    assetsDir: "",
    manifest: true,
    emptyOutDir: true,
    target: "es2015",
    rollupOptions: {
      // loader: { ".js": "jsx" },
      input: {
        main: resolve("./static/src/js/main.jsx"),
      },
      output: {
        // chunkFileNames: "chunks/[hash:25].js",
        chunkFileNames: undefined,
      },
    },
  },
});
