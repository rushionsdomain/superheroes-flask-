import { Link } from "react-router-dom";
import "./Header.css"; // Importing the CSS file

function Header() {
  return (
    <header>
      <h1>
        <Link to="/">Super Heroes</Link>
      </h1>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/heroes">Heroes</Link>
          </li>
          <li>
            <Link to="/powers">Powers</Link>
          </li>
          <li>
            <Link to="/hero_powers/new">Add Hero Power</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
