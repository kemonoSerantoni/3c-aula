import React from "react";
import {render, screen} from "@testing-library/react";
import UserList from "./UserList";

test("deve exibir um texto de loading", () => {
    render(<UserList/>);
    expect(screen.getByText("Loading...")).toBeInTheDocument();
});