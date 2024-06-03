import React from 'react';
import { Layout } from 'antd';

const { Sider } = Layout;

function SidebarComponent() {
  return (
    <Sider width="15%" style={{ background: '#fff' }}>
      sidebar content here yo
    </Sider>
  );
}

export default SidebarComponent;
