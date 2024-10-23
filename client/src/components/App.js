import { Switch, Route } from "react-router-dom";
import Header from "./Header";
import Hero from "./Hero";
import Home from "./Home";
import HeroPowerForm from "./HeroPowerForm";
import Power from "./Power";
import PowerEditForm from "./PowerEditForm";
import HeroesList from "./HeroesList"; // Import the HeroesList component

function App() {
  return (
    <div>
      <Header />
      <main>
        <Switch>
          <Route exact path="/hero_powers/new">
            <HeroPowerForm />
          </Route>
          <Route exact path="/powers/:id/edit">
            <PowerEditForm />
          </Route>
          <Route exact path="/powers/:id">
            <Power />
          </Route>
          <Route exact path="/heroes/:id">
            <Hero />
          </Route>
          <Route exact path="/heroes">
            {" "}
            {/* Add a new route for HeroesList */}
            <HeroesList />
          </Route>
          <Route exact path="/">
            <Home />
          </Route>
        </Switch>
      </main>
    </div>
  );
}
export default App;
