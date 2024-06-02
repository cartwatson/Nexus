import React from 'react';
import { Layout } from 'antd';
import HeaderComponent from './components/Header';
import SidebarComponent from './components/Sidebar';
import ContentComponent from './components/Content';
import FooterComponent from './components/Footer';

const App: React.FC = () => {
    return (
        <Layout style={{ minHeight: '100vh' }}>
            <HeaderComponent />
            <Layout>
                <SidebarComponent />
                <ContentComponent />
            </Layout>
            <FooterComponent />
        </Layout>
    );
};

export default App;

