import React from 'react';
import { Layout } from 'antd';

const { Footer } = Layout;

const FooterComponent: React.FC = () => {
    return (
        <Footer>
          <div>©Created by <a href="https://github.com/cartwatson">Carter Watson</a></div>
        </Footer >
    );
};

export default FooterComponent;

