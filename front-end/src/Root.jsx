import React, { useState } from "react";
import CodeContainer from "./pages/CodeContainer";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Navbar from "./components/templates/MainNavbar";
import MainContainer from "./pages/MainContainer";
import IntroContainer from "./pages/IntroContainer";
import SignUpContainer from "./pages/SignUpContainer";
import MyClassContainer from "./pages/MyClassContainer";
import CommunityContainer from "pages/CommunityContainer";
import AskContainer from "./pages/AskContainer";
import CodeResultContainer from "./pages/CodeResultContainer";
import MessageContainer from "./pages/MessageContainer";
import MyPageContainer from "./pages/MyPageContainer";
import ClassContainer from "./pages/ClassContainer";
import SendMessageContainer from "./pages/SendMessageContainer";


const Root = () => {
  const [userType, setUserType] = useState(window.sessionStorage.getItem('userType'));

  return (
    <Router>
      <Navbar userType={userType}/>
      <Switch>
        <Route exact path="/"       component={MainContainer} />
        <Route path="/start"        component={CodeContainer} />
        <Route path="/about"        component={IntroContainer} />
        <Route path="/signup"       component={SignUpContainer} />
        <Route path="/myclass"      component={MyClassContainer} />
        <Route path="/ask"          component={AskContainer} />
        <Route path="/community"    component={CommunityContainer} />
        <Route path="/result"       component={CodeResultContainer} />
        <Route path="/message"      component={MessageContainer} />
        <Route path="/mypage"       component={MyPageContainer} />
        <Route path="/class"        component={ClassContainer} />
        <Route path="/sendMessage"  component={SendMessageContainer} />
      </Switch>
    </Router>
  );
};

export default Root;