// builtin components
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Layout } from 'antd';

// layout components
import HeaderComponent from './components/layouts/Header';
import SidebarComponent from './components/layouts/Sidebar'; 
import FooterComponent from './components/layouts/Footer';

import { HomeDashboard, SatelliteDashboard, DroidsDashboard, ImagesDashboard } from './components/layouts/dashboards'; 

const App: React.FC = () => {
    return (
        <Layout style={{ minHeight: '100vh' }}>
            <HeaderComponent />
            <Layout>
                <Router>
                    <Switch>
                        <Route path="/" component={HomeDashboard} />
                        <Route path="/satellites" component={SatelliteDashboard} />
                        <Route path="/droids" component={DroidsDashboard} />
                        <Route path="/images" component={ImagesDashboard} />
                    </Switch>
                </Router>
                <SidebarComponent />
            </Layout>
            <FooterComponent />
        </Layout>
    );
};

export default App;

