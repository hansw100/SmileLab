import React from "react";
import { Table } from "react-bootstrap";
import TableHeader from "../molecules/table/TableHeader";
import TableBody from "../molecules/table/TableBody";

const ResponsiveTable = ({ headers, rows }) => {
  return (
    <Table responsive>
      <TableHeader headers={headers} />
      <TableBody rows={rows} />
    </Table>
  );
};

export default ResponsiveTable;
