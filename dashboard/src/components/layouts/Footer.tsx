import React from 'react';
import { Layout } from 'antd';

const { Footer } = Layout;

const FooterComponent: React.FC = () => {
    return (
        <Footer>
          <div>© 2024 <a href="https://github.com/cartwatson">Carter Watson</a></div>
        </Footer >
    );
};

export default FooterComponent;

