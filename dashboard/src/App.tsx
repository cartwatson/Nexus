// builtin components
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Layout } from 'antd';

// TODO: move into modules
// layouts
import HeaderComponent from './components/layouts/Header';
import SidebarComponent from './components/layouts/Sidebar'; 
import FooterComponent from './components/layouts/Footer';

// dashboards
import HomeDashboard from './components/layouts/dashboards/HomeDashboard';
import SatelliteDashboard from './components/layouts/dashboards/SatelliteDashboard'; 
import DroidsDashboard from './components/layouts/dashboards/DroidsDashboard'; 
import ImagesDashboard from './components/layouts/dashboards/ImagesDashboard';

const App: React.FC = () => {
    return (
        <Router>
            <Layout style={{ minHeight: '100vh' }}>
                <HeaderComponent />
                <Layout>
                    {/*<SidebarComponent />*/}
                        <Switch>
                            <Route exact path="/" component={HomeDashboard} />
                            <Route path="/satellites" component={SatelliteDashboard} />
                            <Route path="/droids" component={DroidsDashboard} />
                            <Route path="/images" component={ImagesDashboard} />
                        </Switch>
                </Layout>
                {/* <FooterComponent /> */}
            </Layout>
        </Router>
    );
};

export default App;

