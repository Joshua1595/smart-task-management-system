import { Outlet } from "react-router-dom";

import Navbar from "../../components/Navbar";
import Sidebar from "../../components/Sidebar";

function DashboardLayout() {
  return (
    <>
      <Navbar />

      <div className="flex">
        <Sidebar />

        <main className="flex-1 p-6 bg-gray-100 min-h-screen">
          <Outlet />
        </main>
      </div>
    </>
  );
}

export default DashboardLayout;